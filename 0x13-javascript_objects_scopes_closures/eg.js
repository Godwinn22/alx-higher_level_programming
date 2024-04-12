class Person {
  name;

  constructor (name) {
    this.name = name;
  }

  introduceSelf () {
    console.log('My name is ' + this.name);
  }
}

class Employee extends Person {
  salary;
  position;
  constructor (name, salary, position) {
    super(name);
    this.salary = salary;
    this.position = position;
  }

  employeeDetails () {
    console.log(
            `This employees name is ${this.name} and he works as a ${this.position}.His salary is ${this.salary}`
    );
  }
}

person1 = new Person('James');
person1.introduceSelf();

emp1 = new Employee('John', 8000, 'Cleric');
emp1.employeeDetails();
console.log(emp1.salary);
console.log(emp1.position);
