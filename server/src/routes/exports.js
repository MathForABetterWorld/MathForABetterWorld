import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/exportsMiddleware.js";
import * as controller from "../controller/exportsController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

export default router;

router.post(
  "/",
  body("weight", "Please include a positive weight exported!")
    .notEmpty()
    .isFloat({ gt: 0.0 }),
  body("categoryId", "Please include the category of the export")
    .notEmpty()
    .isInt(),
  body(
    "donatedTo",
    "Please include the person/location this was donated to"
  ).notEmpty(),
  body("userId", "Please include the user id that distributed this!")
    .notEmpty()
    .isInt(),
  body("locationId", "LocationId must be an integer").optional().isInt(),
  validator.isUserId,
  validator.isCategoryId,
  validator.isLocationIdOptional,
  controller.createExport
);

router.get("/", controller.getExports);

router.delete(
  "/:id",
  param("id", "Please include id of export to delete").notEmpty().isInt(),
  validator.isExportIdParam,
  controller.deleteExport
);

router.post(
  "/edit",
  body("id", "Please include an id of the exportItem!").notEmpty().isInt(),
  body("weight", "Please include a positive weight exported!")
    .notEmpty()
    .isFloat({ gt: 0.0 }),
  body("categoryId", "Please include the category of the export")
    .notEmpty()
    .isInt(),
  body(
    "donatedTo",
    "Please include the person/location this was donated to"
  ).notEmpty(),
  body("userId", "Please include the user id that distributed this!")
    .notEmpty()
    .isInt(),
  body("locationId", "LocationId must be an integer").optional().isInt(),
  validator.isExportId,
  validator.isUserId,
  validator.isCategoryId,
  validator.isLocationIdOptional,
  controller.createExport
);

router.get(
  "/inPast/:duration",
  param("duration", "Please include a duration filter")
    .notEmpty()
    .isIn(["day", "week", "month", "year"]),
  controller.getExportsInDuration
);
