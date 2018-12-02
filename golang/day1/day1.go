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
	input, err := ioutil.ReadFile("input.txt")

	if err != nil {
		log.Panicf("Could not read file, %s", err)
	}
	scanner := bufio.NewScanner(bytes.NewReader(input))
	freq := 0
	for scanner.Scan() {
		tmpResult := parseLine(scanner.Text())
		freq += tmpResult
	}
	fmt.Printf("Part1: Final frequency is %d\n", freq)

	freq = 0
	freqCache := make(map[int]struct{})
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
