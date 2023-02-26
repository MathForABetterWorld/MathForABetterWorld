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
  validator.isRackId,
  controller.createRack
);

router.get("/", controller.getDistributors);

router.delete(
  "/:id",
  validator.isUniqueLocation,
  validator.isRackId,
  controller.deleteRack
);

router.post(
  "/update",
  validator.isUniqueLocation,
  validator.isRackId,
  controller.updateRack
);


export default router;
