import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/categoryMiddleware.js";
import * as controller from "../controller/categoryController";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud


router.post(
    "/",
    body("name", "Must include unique name for category").notEmpty(),
    validator.isUniqueName,
    controller.createCategory
  );

router.get("/", controller.getCategory);

router.delete(
    "/:id",
    param("id", "Must include id in the url params").notEmpty().isInt(),
    validator.isCategoryId,  
    controller.deleteCategory
  );

router.post(
    "/update",
    body("name", "Must include name in the request").notEmpty(),
    param("id", "Must include id in the body").notEmpty().isInt(),
    validator.isUniqueName,
    validator.isCategoryId,
    controller.updateCategory
  );

export default router;