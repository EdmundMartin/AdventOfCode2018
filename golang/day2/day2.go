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
	return countExists(info, 2), countExists(info, 3)
}

func solvePartOne(input []byte) {
	firstCount, secoundCount := 0, 0
	scanner := bufio.NewScanner(bytes.NewReader(input))
	for scanner.Scan() {
		two, three := parseLine(scanner.Text())
		firstCount += two
		secoundCount += three
	}
	result := firstCount * secoundCount
	fmt.Printf("Part 1: result is %d\n", result)
}

type Record struct {
	Chars []string
	Len   int
}

func difference(s1 []string, s2 []string) int {
	diff := 0
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			diff++
		}
	}
	return diff
}

func sharedChars(s1 []string, s2 []string) string {
	finalString := ""
	for i := 0; i < len(s1); i++ {
		if s1[i] == s2[i] {
			finalString += s1[i]
		}
	}
	return finalString
}

func solvePartTwo(input []byte) {
	all := []Record{}
	scanner := bufio.NewScanner(bytes.NewReader(input))
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.Trim(line, "\n")
		record := Record{Chars: strings.Split(line, ""), Len: len(line)}
		all = append(all, record)
	}
	for _, rcd := range all {
		for _, rcd2 := range all[1:] {
			diff := difference(rcd.Chars, rcd2.Chars)
			//fmt.Println(diff)
			if diff == 1 {
				fmt.Printf("Part two result is: %s\n", sharedChars(rcd.Chars, rcd2.Chars))
				return
			}
		}
	}
}

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatalf("Encountered fatal error, %s", err)
	}
	solvePartOne(input)
	solvePartTwo(input)
}
