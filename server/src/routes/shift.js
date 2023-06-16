import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/shiftMiddleware.js";
import * as controller from "../controller/shiftController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();

router.post(
  "/",
  body("userId", "Please include a user id for the shift").notEmpty().isInt(),
  body("start", "Please include a start time").notEmpty().isISO8601(),
  validator.isUserId, // make sure user exists
  //validator.isValidTimeShift,
  controller.createShift
);

router.post(
  "/signout",
  body("id", "id must be an int").notEmpty().isInt(),
  validator.isShiftIdBody,
  controller.signout
);

router.get("/", controller.getShift);

router.delete("/:id", validator.isShiftId, controller.deleteShift);

router.post(
  "/update",
  body("id", "id must be an int").notEmpty().isInt(),
  body("userId", "userId must be an int").notEmpty().isInt(),
  body("start", "Please include a start time").notEmpty().isISO8601(),
  body("end", "Please include an end time").notEmpty().isISO8601(),
  validator.isUserId, // make sure user exists
  //validator.isValidTimeShift,
  validator.isShiftIdBody, // make sure shift exists
  controller.updateShift
);

// get total number of hours worked accross all volunteers
router.get("/totalVolunteerHours", controller.getTotalHoursWorked);

router.get("/activeshifts", controller.getActiveShifts);

router.get(
  "/startDate/:startDate/endDate/:endDate",
  validator.startIsBeforEnd,
  controller.getShiftsInRange
);

export default router;
