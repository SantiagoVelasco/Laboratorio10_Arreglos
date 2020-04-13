package main

import (
	"fmt"
)

func main(){
	var n int
		fmt.Println("Ingrese el número de la variable n: ")
		fmt.Scanln(&n)
	c := 0
	for j:=1; j<n; j = j+1{
		if (n%j)==0{
			c = c + j
		}
	}
	if c == n{
		fmt.Println(" N es un número perfecto")
	}else {
		fmt.Println("N no es un número perfecto")
	}
}