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
  param('id', 'Please include an integer for id').notEmpty().isInt(),
  validator.isRackId, // this validator assumes your rackId is in the params, so either add it there or create a new middleware for checking it from the body
  controller.deleteRack
);

router.post(
  "/update/:id",
  param('id', 'Please include an integer for id').notEmpty().isInt(),
  body('location', 'location must be a string').notEmpty().isString(),
  body('description', "description must be a string").notEmpty().isString(),
  body('weightLimit', 'weightLimit must be a float').optional().isFloat(),
  validator.isUniqueLocation,
  validator.isRackId, // this validator assumes your rackId is in the params, so either add it there or create a new middleware for checking it from the body
  controller.updateRack
);


export default router;
