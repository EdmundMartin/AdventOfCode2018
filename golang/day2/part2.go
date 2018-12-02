package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

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

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatalf("Encountered fatal error, %s", err)
	}
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
				fmt.Println("diff 1 found")
				fmt.Printf("result %s", sharedChars(rcd.Chars, rcd2.Chars))
				return
			}
		}
	}
}
