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
	fmt.Printf("Final frequency is %d", freq)
}
