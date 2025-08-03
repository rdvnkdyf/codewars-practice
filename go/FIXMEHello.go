package kata

import (
	"fmt"
	"strings"
)

// Dinglemouse struct now includes fields to track
// which attributes have been set and their order.
type Dinglemouse struct {
	name string
	age  int
	sex  rune

	// To track the order of first assignment
	// We'll store a list of attribute names in the order they were first set.
	setOrder []string

	// To quickly check if an attribute has been set for the first time
	// and to prevent adding it to setOrder multiple times.
	isSet map[string]bool
}

// NewDinglemouse initializes a new Dinglemouse object.
// It also initializes the setOrder slice and the isSet map.
func NewDinglemouse() *Dinglemouse {
	return &Dinglemouse{
		setOrder: []string{},
		isSet:    make(map[string]bool),
	}
}

// addSetAttribute is a helper to record the order of first assignment.
func (d *Dinglemouse) addSetAttribute(attrName string) {
	if !d.isSet[attrName] {
		d.setOrder = append(d.setOrder, attrName)
		d.isSet[attrName] = true
	}
}

// SetAge sets the age attribute and records its assignment order.
func (d *Dinglemouse) SetAge(age int) *Dinglemouse {
	d.age = age
	d.addSetAttribute("age")
	return d
}

// SetSex sets the sex attribute and records its assignment order.
func (d *Dinglemouse) SetSex(sex rune) *Dinglemouse {
	d.sex = sex
	d.addSetAttribute("sex")
	return d
}

// SetName sets the name attribute and records its assignment order.
func (d *Dinglemouse) SetName(name string) *Dinglemouse {
	d.name = name
	d.addSetAttribute("name")
	return d
}

// Hello generates the greeting based on explicitly set attributes
// and their first assignment order.
func (d *Dinglemouse) Hello() string {
	parts := []string{"Hello."} // Start with the mandatory greeting

	// Iterate through the attributes in the order they were first set.
	for _, attr := range d.setOrder {
		switch attr {
		case "name":
			parts = append(parts, fmt.Sprintf("My name is %s.", d.name))
		case "age":
			parts = append(parts, fmt.Sprintf("I am %d.", d.age))
		case "sex":
			sexText := "male"
			if d.sex == 'F' {
				sexText = "female"
			}
			parts = append(parts, fmt.Sprintf("I am %s.", sexText))
		}
	}
	return strings.Join(parts, " ")
}