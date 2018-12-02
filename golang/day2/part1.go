package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func countExists(data map[rune]int, target int) int {
	for _, v := range data {
		if v == target {
			return 1
		}
	}
	return 0
}

func parseLine(target string) (int, int) {
	line := strings.TrimSuffix(target, "\n")
	info := make(map[rune]int)
	for _, t := range line {
		_, exists := info[t]
		if exists {
			info[t]++
		} else {
			info[t] = 1
		}
	}
	fmt.Println(info)
	return countExists(info, 2), countExists(info, 3)
}

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatalf("Encountered fatal error, %s", err)
	}
	firstCount, secoundCount := 0, 0
	scanner := bufio.NewScanner(bytes.NewReader(input))
	for scanner.Scan() {
		two, three := parseLine(scanner.Text())
		firstCount += two
		secoundCount += three
	}
	result := firstCount * secoundCount
	fmt.Printf("result is %d", result)
}
