#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This function displays ever RGB value using nested
#      loops


def main():
    # This function displays ever RGB value using nested
    #       loops

    print("This program displays every RGB value from "
          "(0,0,0) to (255,255,255).")

    # variable declarations
    counter_r = 0
    counter_g = 0
    counter_b = 0

    # process
    for counter_r in range(256):
        for counter_g in range(256):
            for counter_b in range(256):
                print("RGB({0},{1},{2})".format(counter_r, counter_g,
                                                counter_b))


if __name__ == "__main__":
    main()
