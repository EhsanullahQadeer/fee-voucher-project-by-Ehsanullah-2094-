import express from "express";
import "./config/dotenv.js";
import { setupExpressMiddleware } from "./api/v1/middlewares/express.middleware.js";
import { connect as databaseConnect } from "./config/database.config.js";
import { initializeRoutes } from "./api/v1/routes/index.js";

const app = express();
setupExpressMiddleware(app);

databaseConnect();

initializeRoutes(app);

const port = process.env.PORT;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
