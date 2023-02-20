import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/foodEntryMiddleware.js";
import * as controller from "../controller/foodEntryController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
  "/",
  //validator.isUniqueName,
  controller.createFoodEntry
);

router.get("/", controller.getFoodEntrys);

router.delete("/:id", validator.isFoodEntryId, controller.deleteFoodEntry);

export default router;
