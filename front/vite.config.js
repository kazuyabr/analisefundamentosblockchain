import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig, loadEnv } from "vite";

export default async () => {
  const env = await loadEnv("", process.cwd()); // Carrega as variáveis de ambiente do arquivo .env

  return defineConfig({
    plugins: [sveltekit()],
    server: {
      // https: {
      //   key: './key.pem',
      //   cert: './cert.pem',
      // },
      port: Number(env.VITE_PORT),
      strictPort: true,
    },
  });
};
