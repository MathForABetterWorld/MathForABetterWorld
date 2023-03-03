import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/pallotMiddleware.js";
import * as controller from "../controller/pallotController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
  '/',
  body('entryUserId', 'Please include an integer for entryUserId').notEmpty().isInt(),
  body('inputDate', 'Please include a date for inputDate').notEmpty().isDate(),
  body('expirationDate', "Expiration Date must be a date").optional().isDate(),
  body('weight', 'Please include a float for entryUserId').notEmpty().isFloat(),
  body('companyId', 'Please include an integer for companyId').notEmpty().isInt(),
  body('rackId', 'Rack must be an int').optional().isInt(),
  body('inWarehouse', 'Please include a boolean for inWarehouse').notEmpty().isBoolean(),
  body('description', 'Description is a string').optional().isString(),
  body('categoryId', 'Please include an integer for categoryId').notEmpty().isInt(),
  validator.isExpired,
  validator.isDistributorId,
  validator.isUserId,
  validator.isRack,
  validator.isCategory,
  validator.isPositiveWeight,
  validator.isWarehouseTrue,
  controller.createPallot,
);

router.post(
  "/edit/:id",
  param('id', 'Please include an integer for pallotId').notEmpty().isInt(),
  body('entryUserId', 'Please include an integer for entryUserId').notEmpty().isInt(),
  body('inputDate', 'Please include a date for inputDate').notEmpty().isDate(),
  body('expirationDate', "Expiration Date must be a date").optional().isDate(),
  body('weight', 'Please include a float for entryUserId').notEmpty().isFloat(),
  body('companyId', 'Please include an integer for companyId').notEmpty().isInt(),
  body('rackId', 'Rack must be an int').optional().isInt(),
  body('inWarehouse', 'Please include a boolean for inWarehouse').notEmpty().isBoolean(),
  body('description', 'Description is a string').optional().isString(),
  body('categoryId', 'Please include an integer for categoryId').notEmpty().isInt(),
  validator.isExpired,
  validator.isDistributorId,
  validator.isUserId,
  validator.isRack,
  validator.isCategory,
  validator.isPositiveWeight,
  validator.isWarehouseTrue,
  controller.edit,
);

router.get("/", controller.getPallots);

router.delete(
  "/:id", 
  param('id', 'Please include an integer for pallotId').notEmpty().isInt(),
  validator.isPallotId, 
  controller.deletePallot
);

export default router;