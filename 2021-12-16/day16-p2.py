"""
--- Part Two ---
Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.

Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:

Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Using these rules, you can now work out the value of the outermost packet in your BITS transmission.

For example:

C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?
"""
from dataclasses import dataclass
import numpy
import time


filename = 'input.txt'
# filename = 'test_input.txt'
# filename = 'test_input2.txt'
# filename = 'test_input3.txt'
data_stream = ''
stream_position = 0
TEST_MODE = True


class EndOfPacket(Exception):
    pass


def get_bits(bits):
    global data_stream, stream_position
    if stream_position + bits > len(data_stream):
        raise EndOfPacket
    output = data_stream[stream_position:stream_position + bits]
    stream_position += bits
    return output


def get_literal_data():
    output = ''
    number = get_bits(5)
    while number[0] == '1':
        output += number[1:]
        number = get_bits(5)
    output += number[1:]
    output_int = int(output, 2)
    return output_int


class Packet:
    def __init__(self):
        self.version = int(get_bits(3), 2)
        self.packet_type = int(get_bits(3), 2)
        self.data = None
        self.length_type = None
        self.data_length = None
        self.sub_packets = []
        self.number_of_sub_packets = None
        self.end = None
        # if self.version == 0:
        #     if self.packet_type == 0:
        #         raise EndOfPacket
        print(f"V: {self.version}, \tT:{self.packet_type}")
        self.get_rest_of_packet()
        self.data = get_value(self)

    def get_rest_of_packet(self):
        if self.packet_type == 4:
            self.data = get_literal_data()
            # self.data_length = len(self.data)
        else:
            self.length_type = int(get_bits(1), 2)
            if self.length_type == 0:
                self.data_length = int(get_bits(15), 2)
                subpacket_end = self.data_length + stream_position
                while stream_position < subpacket_end:
                    try:
                        self.sub_packets.append(Packet())
                    except EndOfPacket:
                        pass
                # self.data = int(get_bits(self.data_length), 2)
            elif self.length_type == 1:
                self.number_of_sub_packets = int(get_bits(11), 2)
                for each in range(self.number_of_sub_packets):
                    # sub_packet = Packet()
                    # sub_packet.get_rest_of_packet()
                    try:
                        self.sub_packets.append(Packet())
                    except EndOfPacket:
                        pass
                    # self.data_length = len(self.sub_packets)
            else:
                raise IOError(f"Undefinited length type - {self.length_type}")
            # self.end = get_bits(3)


def get_data():
    global stream_position
    output = []
    with open(filename, 'r') as file:
        data_line = file.readlines()
    for line in data_line:
        new_line = line.strip('\n')
        output_line = ''
        for character in new_line:
            output_line += format(int(character, 16), '04b')
        output.append(output_line)
    return output


def count_versions(packet_object: Packet):
    output = packet_object.version
    for sub in packet_object.sub_packets:
        output += count_versions(sub)
    return output


def get_value(packet_obj: Packet):
    if packet_obj.packet_type == 4:
        # Literal value
        return packet_obj.data
    if packet_obj.packet_type == 0:
        # Sum value
        output = 0
        for subp in packet_obj.sub_packets:
            output += subp.data
        return output
    if packet_obj.packet_type == 1:
        # Product
        output = 1
        for subp in packet_obj.sub_packets:
            output *= subp.data
        return output
    if packet_obj.packet_type == 2:
        # minimum
        sub_data = []
        for subp in packet_obj.sub_packets:
            sub_data.append(subp.data)
        return min(sub_data)
    if packet_obj.packet_type == 3:
        # maximum
        sub_data = []
        for subp in packet_obj.sub_packets:
            sub_data.append(subp.data)
        return max(sub_data)
    if packet_obj.packet_type == 5:
        # minimum
        sub_data = []
        if packet_obj.sub_packets[0].data > packet_obj.sub_packets[1].data:
            return 1
        else:
            return 0
    if packet_obj.packet_type == 6:
        # minimum
        sub_data = []
        if packet_obj.sub_packets[0].data < packet_obj.sub_packets[1].data:
            return 1
        else:
            return 0
    if packet_obj.packet_type == 7:
        # minimum
        sub_data = []
        if packet_obj.sub_packets[0].data == packet_obj.sub_packets[1].data:
            return 1
        else:
            return 0


start = time.time()

all_data = get_data()


stream_position = 0
for i in range(len(all_data)):
    data_stream = all_data[i]
    stream_position = 0
    # while len(data_stream) - stream_position > 0:
    # data_stream = data_stream[2:]
    data_length = len(data_stream)
    packets = []

    print(f"Data Stream Length: {len(data_stream)}")

    while stream_position < len(data_stream):
        try:
            packet = Packet()
            # packet.get_rest_of_packet()
            # print(f"Packet Length: {packets.data_length}")
            packets.append(packet)
            # print(f"Stream Position: {stream_position}")
        except EndOfPacket:
            # packets.append(packet)
            print("End of Packet")
            break

    packet_data = []
    total_of_versions = 0
    for pack in packets:
        total_of_versions += count_versions(pack)
        packet_data.append(pack.data)
        print(f"Packet value: \t{packet_data[-1]}")

    print(f"Sum of values:   \t{sum(packet_data)}")
    print(f"Sum of versions: \t{total_of_versions}")

    print(f"Complete: {(time.time() - start):.2f}")
