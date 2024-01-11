import mongoose, { Schema } from "mongoose";

const studentSchema = new Schema({
  studentName: { type: String, required: true },
  fatherName: { type: String, required: true },
  class: { type: String, required: true },
  dateOfBirth: { type:String , required: true },
  rollNo: { type: String, required: true, unique: true },
  tutionFee: { type: Number, required: true },
  annualFee: { type: Number, required: true },
  examinationFee: { type: Number, required: true },
});

export default mongoose.model("student", studentSchema);
