function getStudents() {
  return JSON.parse(localStorage.getItem("students")) || [];
}

function addStudent(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const roll = document.getElementById("roll").value;
  const dept = document.getElementById("dept").value;

  const students = getStudents();
  students.push({ name, roll, dept });

  localStorage.setItem("students", JSON.stringify(students));

  alert("Student Added Successfully!");
  window.location.href = "index.html";
}

function displayStudents() {
  const students = getStudents();
  const table = document.getElementById("studentTable");

  table.innerHTML = "";

  students.forEach(s => {
    table.innerHTML += `
      <tr>
        <td>${s.name}</td>
        <td>${s.roll}</td>
        <td>${s.dept}</td>
      </tr>`;
  });
}

function groupByDepartment() {
  const students = getStudents();
  const deptDiv = document.getElementById("deptList");

  const grouped = {};

  students.forEach(s => {
    if (!grouped[s.dept]) grouped[s.dept] = [];
    grouped[s.dept].push(s.name);
  });

  deptDiv.innerHTML = "";

  for (let dept in grouped) {
    deptDiv.innerHTML += `
      <div>
        <strong>${dept}</strong><br>
        ${grouped[dept].join(", ")}
      </div>`;
  }
}
