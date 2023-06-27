import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/trashMiddleware.js";
import * as controller from "../controller/trashController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
    "/",
    body("weight", "PLease include a positive weight deleted!")
        .notEmpty()
        .isFloat({gt: 0.0}),
    body("categoryId", "Please include an integer category Id")
        .notEmpty()
        .isInt(),
    body("userId", "Please include an integer user ID")
        .notEmpty()
        .isInt(),

    validator.isCategoryId, 
    validator.isUserId,
    controller.createTrash
);

router.get("/", controller.getTrash);

router.post( //for this one I copied the body part the same as the create...which seems like the rightthing to do based on other files and like common sense but want to check
    "/edit",
    body("id", "Pleasue include an id of the trashItem!")
        .notEmpty()
        .isInt(), //check this!
    body("weight", "PLease include a positive weight deleted!")
        .notEmpty()
        .isFloat({gt: 0.0}),
    body("categoryId", "Please include an integer category Id")
        .notEmpty()
        .isInt(),
    body("userId", "Please include an integer user ID")
        .notEmpty()
        .isInt(),
    body("trashDate", "Please include a date").notEmpty().isDate(),
    validator.isCategoryId, 
    validator.isUserId,
    controller.createTrash
);

router.delete(
    "/:id", 
    param("id", "Please include an id of the trash to delete")
        .notEmpty()
        .isInt(),
    validator.isTrashIdParam,
    controller.deleteTrash
);

router.get(
    "/inPast/:duration",
    param("duration", "Please include a duration filter")
      .notEmpty()
      .isIn(["day", "week", "month", "year"]),
    controller.getExportsInDuration
  );

export default router;