import express from "express";
import morgan from "morgan";
import cors from "cors";
import helmet from "helmet";
import user from "./routes/user.js";
import distributor from "./routes/distributor.js";
import foodEntry from "./routes/foodEntry.js";
import category from "./routes/category.js";
import rack from "./routes/rack.js";
import shift from "./routes/shift.js";

import { globalErrorHandler } from "./util/middleware.js";

const app = express();

app.use(cors());
app.use(helmet());
app.use(express.json());
app.use(morgan("dev", { skip: () => process.env.NODE_ENV === "test" }));

app.get("/", (req, res) => {
  res.send("API Server!");
});

// Routing (API endpoints)
app.use("/api", user);
app.use("/api/distributor", distributor);
app.use("/api/food", foodEntry);
app.use("/api/category", category);
app.use("/api/rack", rack);
app.use("/api/shift", shift);

app.use(globalErrorHandler);

export default app;
