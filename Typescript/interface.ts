export interface Address<T> {
    id: number;
    addr1: string;
    addr2?: string;
    city: string;
    pin?: number,
    data: T;
}

// Optional parameters (?) could be skipped, data type must be provided
let address: Address<number> = {
    id: 1,
    addr1: "Somewhere in India.",
    city: "Lucknow",
    data: 100
}


let address2: Required<Address<number>> = {
    id: 2,
    addr1: "Ansal",
    city: "Lucknow",
    data: 200,
    addr2: "Celebrity Green",
    pin: 123
}

let address3: Partial<Address<number>> = {
    id: 2
};

let address4: Readonly<Address<string>> = {
    id: 3,
    addr1: "Ansal",
    city: "Lucknow",
    data: "200",
}

address4.id = 4  // Shows error due to Readonly
address2.data = 500



interface Employees {
    id: number,
    email: string,
    dob: Date,
    department: string,
    name: string,
    salary: number,
    data: string,
}

let empList: Employees[] = [
  {
    id: 1,
    email: "test1@gmail.com",
    dob: new Date("11-Mar-1986"),
    department: "IT",
    name: "test1",
    salary: 10000,
    data: "",
  },
  {
    id: 2,
    email: "test2@gmail.com",
    dob: new Date("11-Mar-1980"),
    department: "IT",
    name: "test2",
    salary: 15000,
    data: "",
  },
  {
    id: 3,
    email: "test1@gmail.com",
    dob: new Date("11-Mar-1990"),
    department: "IT",
    name: "test3",
    salary: 20000,
    data: "",
  },
];

// Array Spreading
let newEmpl: Employees = {
    id: 4,
    email: "test2@gmail.com",
    dob: new Date("11-Mar-1990"),
    department: "IT",
    name: "test4",
    salary: 20000,
    data: "secret",
}

let newEmpList = [...empList, newEmpl];