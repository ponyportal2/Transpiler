package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func HasSuffixes(s, suffix string) bool {
	return len(s) >= len(suffix) && s[len(s)-len(suffix):] == suffix
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println(os.Stderr, "not enough args")
		os.Exit(-1)
	}
	//old, neu := os.Args[1], os.Args[2]
	theFile, err := ioutil.ReadFile(os.Args[3])
	if err != nil {
		log.Fatalln(err)
	}
	// ------------------------------------------
	lines := strings.Split(string(theFile), "\n")

	for i, line := range lines {
		tLine := line

		if tLine == "end" {
			lines[i] = "}"
			continue
		}

		// Trimming whitespaces at the end
		tLine = strings.TrimRight(tLine, "\t \n")

		// : -> {
		if strings.HasSuffix(tLine, ":") {
			if !strings.HasSuffix(tLine, "::") {
				tLine = strings.TrimSuffix(tLine, ":")
				tLine += " {"
			}
		}

		// end -> }
		if strings.HasSuffix(tLine, "end") {
			tLine = strings.TrimSuffix(tLine, "end")
			tLine += "}"
		}

		// One line import
		if strings.HasPrefix(tLine, "import") && !strings.Contains(tLine, "(") && !strings.HasSuffix(tLine, ":") {
			temp := strings.Split(tLine, " ")
			tLine = "import \"" + temp[1] + "\""
		}

		if (strings.HasPrefix(tLine, "    ") || strings.HasPrefix(tLine, "\t")) && strings.HasSuffix(tLine, "\"") {
			tLine = strings.ReplaceAll(tLine, "\"", "")
		}

		// def -> func
		if strings.HasPrefix(tLine, "def") {
			tLine = strings.Replace(tLine, "def", "func", 1)
		}

		// print -> fmt.Println
		if strings.Contains(tLine, "print(") {
			tLine = strings.ReplaceAll(tLine, "print(", "fmt.Println(")
		}

		// printf -> fmt.Printf
		if strings.Contains(tLine, "printf(") {
			tLine = strings.ReplaceAll(tLine, "print(", "fmt.Printf(")
		}

		lines[i] = tLine
	}

	// ------------------------------------------
	filePath, err := filepath.Abs(os.Args[3])
	if err != nil {
		log.Fatalln(err)
	}

	output := strings.Join(lines, "\n")
	out := ioutil.WriteFile(filePath, []byte(output), 0644)
	if out != nil {
		log.Fatalln(err)
	}
}
