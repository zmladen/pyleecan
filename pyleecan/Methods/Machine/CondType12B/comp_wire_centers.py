from numpy import exp, pi, sqrt, sin, cos, array, mean


def comp_wire_centers(self):
    """Calculate the centers for each wire inside conductor

    https://math.stackexchange.com/questions/1283085/hexagon-packing-in-a-circle

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    center_list:
        List of centers for each single wire inside conductor
    """

    # Compute the center of the wire
    center_list = []

    if self.Nwppc == 1:
        center_list.append((0, 0))
    elif self.Nwppc == 2:
        center_list.append((0, self.Wwire / 2 + self.Wins_wire))
        center_list.append((0, -self.Wwire / 2 - self.Wins_wire))
    elif self.Nwppc == 3:
        R = (self.Wwire + 2 * self.Wins_wire) * sqrt(3) / 3.0
        center_list.append((0, R))
        Z2 = R * 1j * exp(1j * 2 * pi / 3)
        Z3 = R * 1j * exp(-1j * 2 * pi / 3)
        center_list.append((Z2.real, Z2.imag))
        center_list.append((Z3.real, Z3.imag))
    elif self.Nwppc == 4:
        a = self.Wwire / 2 + self.Wins_wire
        center_list.append((a, a))
        center_list.append((a, -a))
        center_list.append((-a, a))
        center_list.append((-a, -a))
    else:
        # # For Nwppc > 4
        # # http://www.jonahkadoko.com/2015/08/21/packing-circles-in-a-big-circle/
        # center_list = []
        # r = (self.Wwire + 2 * self.Wins_wire) / 2  # Radius of small circles
        # R = self.comp_width() / 1  # Radius of the big circle
        # delta_x = 2 * r
        # delta_y = r * sqrt(3)

        # positions = []
        # y = -R + r
        # while y <= R - r:
        #     x_offset = 0 if int(round((y + R) / delta_y)) % 2 == 0 else r
        #     x = -R + r + x_offset
        #     while x <= R - r:
        #         distance = sqrt(x**2 + y**2)
        #         if distance + r <= R:
        #             positions.append((distance, (x, y)))
        #         x += delta_x
        #     y += delta_y

        # # Sort positions by distance from center and select up to Nwppc
        # positions.sort()
        # for pos in positions[: self.Nwppc]:
        #     center_list.append(pos[1])

        # https://math.stackexchange.com/questions/1283085/hexagon-packing-in-a-circle
        d = 2 * (self.Wwire / 2 + self.Wins_wire)

        # Base vectors
        u0 = (d * 1, d * 0)
        u1 = (d * 0.5, d * sqrt(3) / 2)

        # Start from the center (0, 0)
        center_list = [(0, 0)]
        counts = 1

        ring = 1
        while counts < self.Nwppc:
            for c0 in range(-ring, ring + 1):
                for c1 in range(-ring, ring + 1):
                    c2 = -c0 - c1  # In hex grids, c0 + c1 + c2 = 0
                    if abs(c0) > ring or abs(c1) > ring or abs(c2) > ring:
                        continue
                    if c0 == 0 and c1 == 0:
                        continue

                    x = c0 * u0[0] + c1 * u1[0]
                    y = c0 * u0[1] + c1 * u1[1]

                    if (x, y) in center_list:
                        continue

                    center_list.append((x, y))
                    counts += 1

                    if counts >= self.Nwppc:
                        break
                if counts >= self.Nwppc:
                    break
            ring += 1

    return center_list
