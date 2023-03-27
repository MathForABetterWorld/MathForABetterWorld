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

router.get("/users", validator.isAdmin, controller.getUsers);

router.post(
  "/promoteUser",
  body("userId", "User id to promote is required").notEmpty().isInt(),
  body("userName", "temp userName is required").notEmpty(),
  body("password", "temp password is required").notEmpty(),
  validator.isUserId,
  validator.isAdmin,
  controller.promoteUser
);

router.post(
  "/promoteToAdmin",
  body("userId", "User id to promote is required").notEmpty().isInt(),
  validator.isUserId,
  validator.isAdmin,
  validator.isUserEmployeeAndNotAdmin,
  controller.promoteToAdmin
);
//need route for edit password/username

router.post(
  "/updateAccount",
  body("newUsername", "new userName is required").notEmpty(),
  body("newPassword", "new password is required").notEmpty(),
  body("userName", "old userName is required").notEmpty(),
  body("password", "old password is required").notEmpty(),
  validator.isUserEmployee,
  validator.loginMatches,
  controller.updateLogin
);

export default router;
