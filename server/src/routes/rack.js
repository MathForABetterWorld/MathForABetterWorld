import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/rackMiddleware.js";
import * as controller from "../controller/rackController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();

router.post(
  "/",
  validator.isUniqueLocation,
  controller.createRack
);

router.get("/", controller.getDistributors);

router.delete(
  "/:id",
  validator.isRackId,
  controller.deleteRack
);

router.post(
  "/update",
  body('id', 'Please include an integer for entryUserId').notEmpty().isInt(),
  body('location', 'Please include a date for inputDate').notEmpty().isString(),
  body('description', "Expiration Date must be a date").notEmpty().isString(),
  body('weightLimit', 'Please include a float for entryUserId').optional().isFloat(),
  validator.isUniqueLocation,
  validator.isRackId,
  controller.updateRack
);


export default router;
