import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/palletMiddleware.js";
import * as controller from "../controller/palletController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
  "/",
  body("entryUserId", "Please include an integer for entryUserId")
    .notEmpty()
    .isInt(),
  body("inputDate", "Please include a date for inputDate").notEmpty().isDate(),
  body("expirationDate", "Expiration Date must be a date").optional().isDate(),
  body("weight", "Please include a float for entryUserId").notEmpty().isFloat(),
  body("companyId", "Please include an integer for companyId")
    .notEmpty()
    .isInt(),
  body("rackId", "Rack must be an int").optional().isInt(),
  body("inWarehouse", "Please include a boolean for inWarehouse")
    .notEmpty()
    .isBoolean(),
  body("description", "Description is a string").optional().isString(),
  body("categoryIds", "Please include an integer for categoryId")
    .notEmpty()
    .isInt(),
  validator.isExpired,
  validator.isDistributorId,
  validator.isUserId,
  validator.isRack,
  validator.isCategory,
  validator.isPositiveWeight,
  validator.isWarehouseTrue,
  controller.createPallet
);

router.post(
  "/edit/:id",
  param("id", "Please include an integer for palletId").notEmpty().isInt(),
  body("entryUserId", "Please include an integer for entryUserId")
    .notEmpty()
    .isInt(),
  body("inputDate", "Please include a date for inputDate").notEmpty().isDate(),
  body("expirationDate", "Expiration Date must be a date").optional().isDate(),
  body("weight", "Please include a float for entryUserId").notEmpty().isFloat(),
  body("companyId", "Please include an integer for companyId")
    .notEmpty()
    .isInt(),
  body("rackId", "Rack must be an int").optional().isInt(),
  body("inWarehouse", "Please include a boolean for inWarehouse")
    .notEmpty()
    .isBoolean(),
  body("description", "Description is a string").optional().isString(),
  body("categoryIds", "Please include an integer for categoryId")
    .notEmpty()
    .isInt(),
  validator.isExpired,
  validator.isDistributorId,
  validator.isUserId,
  validator.isRack,
  validator.isCategory,
  validator.isPositiveWeight,
  validator.isWarehouseTrue,
  controller.edit
);

router.get("/", controller.getPallets);

// get total number of pallets function from palletController.js
router.get("/totalNumberOfPallets", controller.getPalletsCount);

router.get("/soonestExpiringPallet", controller.getSoonestExpiringPallet);

router.delete(
  "/:id",
  param("id", "Please include an integer for palletId").notEmpty().isInt(),
  validator.isPalletId,
  controller.deletePallet
);

router.get("/category/:categoryId", controller.getPalletsForCategory);

router.get("/categories/:id", controller.getCategoriesForPallet);

router.get("/weightperday", controller.returnWeightPerDay);

router.post(
  "/removePallet",
  body("id", "Please include an integer for palletId").notEmpty().isInt(),
  validator.isPalletIdBody,
  validator.notInWarehouse,
  controller.removePallet
);

export default router;
