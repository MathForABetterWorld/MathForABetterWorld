import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/distributorMiddleware.js";
import * as controller from "../controller/distributorController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
const endpoint = "/distributor";

// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
  "/",
  body("name", "Must include name in the request").notEmpty(),
  validator.isUniqueName,
  controller.createDistributor
);

router.get("/", controller.getDistributors);

router.delete(
  "/:id",
  param("id", "Must include id in the url params").notEmpty().isInt(),
  validator.isDistributorId,
  controller.deleteDistributor
);

router.post(
  "/update",
  body("name", "Must include name in the request").notEmpty(),
  param("id", "Must include id in the body").notEmpty().isInt(),
  validator.isUniqueName,
  validator.isDistributorId,
  controller.updateDistributor
);
