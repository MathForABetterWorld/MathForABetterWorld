import express from "express";
import * as express_validator from "express-validator";
import * as validator from "../util/userMiddleware.js";
import * as controller from "../controller/userController.js";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Here the routes will be listed with correspodning middleware

// Example routes from another app:
router.post(
  "/signup",
  body("email", "Email is required").notEmpty().isEmail(),
  body("name", "Name is required").notEmpty(),
  validator.isUniqueEmail,
  controller.create
);

router.get("/", controller.get);

router.post(
  "/update",
  body("email", "Email is required").notEmpty().isEmail(),
  body("id", "Id is required").notEmpty().isInt(),
  validator.isUniqueEmail,
  controller.update
);

// get total number of hours worked accross all volunteers
router.get("/totalUserHours", controller.getTotalUserHours);
export default router;
