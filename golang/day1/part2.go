package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
)

func parseLine(line string) int {
	res, err := strconv.Atoi(line)
	if err == nil {
		return res
	}
	return 0
}

func main() {
	freq := 0
	freqCache := make(map[int]struct{})

	input, err := ioutil.ReadFile("input.txt")

	if err != nil {
		log.Panicf("Could not read file, %s", err)
	}

	for {
		scanner := bufio.NewScanner(bytes.NewReader(input))

		for scanner.Scan() {
			delta := parseLine(scanner.Text())
			freq += delta

			if _, exists := freqCache[freq]; !exists {
				freqCache[freq] = struct{}{}
				continue
			}
			fmt.Printf("Part2: The first frequency to be seen twice is %d\n", freq)
			return
		}
	}
}
