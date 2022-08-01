import NextAuth from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import axios from "axios";

const settings = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      authorization: {
        params: {
          prompt: "consent",
          access_type: "offline",
          response_type: "code",
        },
      },
    }),
  ],
  callbacks: {
    async signIn(user, account, profile) {
      console.log("account");
      console.log(account);
      if (account.provider == "google") {
        const { accessToken, idToken } = account;
        console.log("ok!!!");
        try {
          const response = await axios.post(
            `${process.env.DJANGO_URL}/api/social/login/google`,
            {
              access_token: accessToken,
              id_token: idToken,
            }
          );
          const { access_token } = response.data;
          user.accessToken = access_token;
          return true;
        } catch (error) {
          return false;
        }
      }
      return false;
    },
    async jwt(token, user, account, profile, isNewUser) {
      if (user) {
        const { accessToken } = user;

        token.accessToken = accessToken;
      }
      return token;
    },
    async session({ session, token, user }) {
      session.accessToken = token.accessToken;
      return session;
    },
  },
};

export default (req, res) => NextAuth(req, res, settings);
