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
  // validator.isShiftId, // You won't have a shiftId yet
  validator.isUserId, // make sure user exists
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
  validator.isUserId, // make sure user exists
  
  validator.isShiftId,
  controller.updateShift
);


export default router;
