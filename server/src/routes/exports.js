import express from "express";
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
  body("weight", "Please include a weight exported!").notEmpty().isFloat(),
  body("categoryId", "Please include the category of the export")
    .notEmpty()
    .isInt(),
  body("userId", "Please include the user id that distributed this!")
    .notEmpty()
    .isInt(),
  body("locationId", "Please include the person/location this was donated to")
    .notEmpty()
    .isInt(),
  body("exportType", "exportType must be a valid export type")
    .notEmpty()
    .isIn(["Regular", "Recycle", "Compost", "Damaged", "Return"]),
  validator.isUserId,
  validator.isCategoryId,
  validator.isLocationId,
  validator.returnIsBCF,
  validator.weightUsuallyPositive,
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
  body("userId", "Please include the user id that distributed this!")
    .notEmpty()
    .isInt(),
  body("locationId", "Please include the person/location this was donated to")
    .notEmpty()
    .isInt(),
  body("exportType", "exportType must be a valid export type")
    .notEmpty()
    .isIn(["Regular", "Recycle", "Compost", "Damaged", "Return"]),
  validator.isExportId,
  validator.isUserId,
  validator.isCategoryId,
  validator.isLocationId,
  validator.returnIsBCF,
  validator.weightUsuallyPositive,
  controller.createExport
);

router.get(
  "/inPast/:duration",
  param("duration", "Please include a duration filter")
    .notEmpty()
    .isIn(["day", "week", "month", "year"]),
  controller.getExportsInDuration
);
