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
  validator.isUserId, // make sure user exists
  validator.isValidTimeShift,
  controller.createShift
);

router.get("/", controller.getShift);

router.delete(
  "/:id",
  validator.isShiftId,
  controller.deleteShift
);

router.post(
  "/update",
  body('id', 'id must be an int').notEmpty().isInt(),
  body('userId', 'userId must be an int').notEmpty().isInt(),
  body('start', "start shift must be a date").notEmpty().isDate(),
  body('end', "start shift must be a date").notEmpty().isDate(),
  body('foodTaken', 'foodTaken should be a float').notEmpty().isFloat(),
  validator.isUserId, // make sure user exists
  validator.isValidTimeShift,
  validator.isShiftId, // make sure shift exists
  controller.updateShift
);


export default router;
