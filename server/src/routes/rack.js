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
  param('id', 'Please include an integer for rackId').notEmpty().isInt(),
  validator.isRackId, // this validator assumes your rackId is in the params, so either add it there or create a new middleware for checking it from the body
  controller.deleteRack
);

router.post(
  "/update/:id",
  param('id', 'Please include an integer for rackId').notEmpty().isInt(),
  body('location', 'Please include a date for inputDate').notEmpty().isString(),
  body('description', "Expiration Date must be a date").notEmpty().isString(),
  body('weightLimit', 'Please include a float for entryUserId').optional().isFloat(),
  validator.isUniqueLocation,
  validator.isRackId, // this validator assumes your rackId is in the params, so either add it there or create a new middleware for checking it from the body
  controller.updateRack
);


export default router;
