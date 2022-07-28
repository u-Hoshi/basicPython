import Head from "next/head";
import "../styles/globals.css";
import Layout from "../components/layout/layout";
import { Provider } from "next-auth/client";

function MyApp({ Component, pageProps }) {
  return (
    <Provider session={pageProps.session}>
      <Layout>
        <Head>
          <meta
            name='viewport'
            content='width-device-width, initial-scale=1'
          ></meta>
        </Head>
        <Component {...pageProps} />
      </Layout>
    </Provider>
  );
}

export default MyApp;
