import Student from "../models/student.js";
export const insertRecord = async (req, res) => {
  console.log("insertRecord: ", req.body);
  try {
    const newStudent = new Student(req.body);
    await newStudent.save();
    res.status(201).json({ message: "Student record inserted successfully" });
  } catch (error) {
    console.error("Error inserting student record:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
export const getRecord = async (req, res) => {
  try {
    const allStudentsRecord = await Student.find();
    console.log("allStudentsRecord: ", allStudentsRecord);
    res.status(200).json({ allStudentsRecord });
  } catch (error) {
    console.error("Error inserting student record:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
export const getSingleRecord = async (req, res) => {
  try {
    const { rollNo } = req.query;
    console.log('rollNo: ', rollNo);

    // Ensure rollNo is provided
    if (!rollNo) {
      return res.status(400).json({ error: "Missing rollNo parameter" });
    }

    const singleRecord = await Student.findOne({ rollNo });

    // Check if a record was found
    if (!singleRecord) {
      return res.status(404).json({ error: "Record not found" });
    }

    res.status(200).json({ singleRecord });
  } catch (error) {
    console.error("Error fetching single student record:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
