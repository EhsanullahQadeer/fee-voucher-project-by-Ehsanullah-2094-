import crudRoutes from "./crud.routes.js";
export const initializeRoutes = (app) => {
  app.use("/api/v1", crudRoutes);
};
