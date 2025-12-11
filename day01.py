import day01_input


class puzzle:
    def make_dial_list(self, input_list):
        dial_list = []
        for line in input_list.splitlines():
            dir = line[0]
            num = int(line[1:])
            dial_list.append((dir, num))
        return dial_list
    
    def __init__(self, input_list):
        self.dial = 50
        self.dial_list = self.make_dial_list(input_list)
        self.password = 0

    def rotate1(self, dir, num):
        if dir == 'L':
            self.dial = (self.dial - num) % 100
        else:
            self.dial = (self.dial + num) % 100

    def rotate2(self, dir, num):
        full_rotations = num // 100
        intra = num - full_rotations * 100
        self.password += full_rotations
        if dir == 'L':
            if self.dial > 0 and self.dial - intra <= 0:
                self.password += 1
            self.dial = (self.dial - intra) % 100
        if dir == 'R':
            if self.dial + intra >= 100:
                self.password += 1
            self.dial = (self.dial + intra) % 100
        return self.password

    def get_password1(self):
        for instruction in self.dial_list:
            self.rotate1(instruction[0], instruction[1])
            # print(self.dial, instruction[0], instruction[1])
            if self.dial == 0:
                self.password += 1
        return self.password

    def get_password2(self):
        for instruction in self.dial_list:
            self.rotate2(instruction[0], instruction[1])
            print(self.dial, instruction[0], instruction[1], self.password)
        return self.password


if __name__ == "__main__":
    p1 = puzzle(day01_input.puzzle)
    # print(p1.dial_list)
    # print(p1.get_password1())
    p2 = puzzle(day01_input.puzzle)
    print(p2.get_password2())