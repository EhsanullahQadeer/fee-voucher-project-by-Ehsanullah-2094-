import express from "express";
const router = express.Router();
import { authenticatePassword } from "../middlewares/auth.middleware.js";
import { login } from "../controllers/auth.controller.js";
import { insertRecord,getRecord ,getSingleRecord} from "../controllers/records.controller.js";
router.post("/auth/login", authenticatePassword, login);
router.post("/insert-record",insertRecord);
router.get("/get-student-record",getRecord);
router.get("/get-single-record",getSingleRecord);

export default router;
