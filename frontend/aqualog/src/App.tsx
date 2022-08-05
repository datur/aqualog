import React, { useState } from 'react';
import SuperTokens, { getSuperTokensRoutesForReactRouterDom } from "supertokens-auth-react";
import EmailPassword from "supertokens-auth-react/recipe/emailpassword";
import Session from "supertokens-auth-react/recipe/session";

import './App.css';
import { Routes, BrowserRouter as Router, Route } from "react-router-dom";
import SessionExpiredPopup from './components/SessionExpiredPopUp/SessionExpiredPopUp';
import Home from './components/Home/Home';
import HomePage from './components/HomePage/HomePage';
import NavBar from './components/NavBar/NavBar';
import NotFound from './components/ErrorPages/NotFound';
import Dashboard from './components/Dashboard/Dashboard';
import AddTank from './components/Tank/EditTank';
import ListTanks from './components/Tank/ListTanks';
import Onboarding from './components/Onboarding/Onboarding';
import ViewTank from './components/Tank/ViewTank';
import Profile from './components/Profile/Profile';
import EditTank from './components/Tank/EditTank';
import AddReading from './components/Reading/AddReading';
import ListReadings from './components/Reading/ListReadings';

export function getApiDomain() {
  const apiPort = process.env.REACT_APP_API_PORT || 3001;
  const apiUrl = process.env.REACT_APP_API_URL || `http://localhost:${apiPort}`;
  return apiUrl;
}

export function getWebsiteDomain() {
  const websitePort = process.env.REACT_APP_WEBSITE_PORT || 3000;
  const websiteUrl = process.env.REACT_APP_WEBSITE_URL || `http://localhost:${websitePort}`;
  return websiteUrl;
}

SuperTokens.init({
  appInfo: {
      appName: "SuperTokens Demo App", // TODO: Your app name
      apiDomain: getApiDomain(), // TODO: Change to your app's API domain
      websiteDomain: getWebsiteDomain(), // TODO: Change to your app's website domain
  },
  recipeList: [
      EmailPassword.init({
          emailVerificationFeature: {
              mode: "REQUIRED",
          },
          getRedirectionURL: async (context) => {
            if (context.action === "SIGN_IN_AND_UP") {
                // called when the user is navigating to sign in / up page
            } else if (context.action === "SUCCESS") {
                // called on a successful sign in / up. Where should the user go next?
                let redirectToPath = context.redirectToPath;
                if (redirectToPath !== undefined) {
                    // we are navigating back to where the user was before they authenticated
                    return redirectToPath;
                }
                if (context.isNewUser) {
                    // user signed up
                    return "/onboarding"
                } else {
                    // user signed in
                    return "/dashboard"
                }
            } else if (context.action === "VERIFY_EMAIL") {
                // called when the user is to be shown the verify email screen
            }
            // return undefined to let the default behaviour play out
            return undefined;
        }
      }),
      Session.init(),
  ],
});

function App() {
  let [showSessionExpiredPopup, updateShowSessionExpiredPopup] = useState(false);
  return (
    <div className="App">
      <Router>
      <div>
        <Routes>
          {/* This shows the login UI on "/auth" route */}
          {getSuperTokensRoutesForReactRouterDom(require("react-router-dom"))}
          {/* Index */}
          <Route
              path="/"
              element={
                <EmailPassword.EmailPasswordAuth
                onSessionExpired={() => {
                  updateShowSessionExpiredPopup(true);
                }}
                requireAuth={false}
                key="index">
                  <NavBar/>
                  <HomePage/>
                  {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* Dashboard */}
          <Route
              path="/dashboard"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="dashboard">
                      <NavBar/>
                      <Dashboard/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* Profile and Settings */}
          {/* View Profile */}
          <Route
              path="/profile"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="profile">
                      <NavBar/>
                      <Profile update={false}/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* Update Profile */}
          <Route
              path="/profile/update"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="profileupdate">
                      <NavBar/>
                      <Profile update={true}/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* Onboarding */}
          <Route
            path="/onboard"
            element={
              <EmailPassword.EmailPasswordAuth
                onSessionExpired={() => {
                  updateShowSessionExpiredPopup(true);
              }}
              requireAuth={true}
              key="onboard">
                <Onboarding/>
                {showSessionExpiredPopup && <SessionExpiredPopup />}
              </EmailPassword.EmailPasswordAuth>
            }
          />

          {/* Tanks */}
          {/* Add Tank */}
          <Route
              path="/tank/add"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="addtank">
                      <NavBar/>
                      <EditTank update={false} currTank={undefined}/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* List Tanks */}
          <Route
              path="/tanks"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="tanks">
                      <NavBar/>
                      <ListTanks/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* View Tank */}
          <Route
              path="/tank/:id"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="viewtank">
                      <NavBar/>
                      <ViewTank/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* Update Tank */}
          <Route
              path="/tank/:id/update"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="updatetank">
                      <NavBar/>
                      <EditTank/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          
          {/* Readings */}
          {/* Add Reading */}
          <Route
              path="/tank/:id/reading/add"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="addtank">
                      <NavBar/>
                      <AddReading/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          <Route
              path="/reading/add"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="addtank">
                      <NavBar/>
                      <AddReading/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          <Route
              path="/tank/:id/readings"
              element={
                <EmailPassword.EmailPasswordAuth
                    onSessionExpired={() => {
                      updateShowSessionExpiredPopup(true);
                    }}
                    requireAuth={true}
                    key="addtank">
                      <NavBar/>
                      <ListReadings/>
                    {showSessionExpiredPopup && <SessionExpiredPopup />}
                </EmailPassword.EmailPasswordAuth>
              }
          />

          {/* <Route
              path="/home"
              element={
                  <EmailPassword.EmailPasswordAuth
                      onSessionExpired={() => {
                          updateShowSessionExpiredPopup(true);
                      }}
                      requireAuth={true}
                      key="home">
                      <Home/>
                      {showSessionExpiredPopup && <SessionExpiredPopup />}
                  </EmailPassword.EmailPasswordAuth>
              }
          /> */}


          <Route path="*" element={<NotFound/>} />
        </Routes>
      </div>
      </Router>
    </div>
  );
}

export default App;
