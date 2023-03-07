import express from "express";
import * as express_validator from "express-validator";
import * as validator from "../util/employeeMiddleware.js";
import * as controller from "../controller/employeeController.js";
import { checkToken } from "../util/middleware.js";
const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Here the routes will be listed with correspodning middleware
router.use(checkToken);

router.post(
  "/promoteUser",
  body("userId", "User id to promote is required").notEmpty().isInt(),
  body("userName", "userName is required").notEmpty(),
  body("password", "password is required").notEmpty(),
  validator.isUserId,
  validator.isAdmin,
  controller.promoteUser
);
//need route for edit password/username

export default router;
