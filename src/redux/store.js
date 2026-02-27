import { createStore, applyMiddleware } from '@reduxjs/toolkit';
import { persistStore, persistReducer } from 'redux-persist';
import { composeWithDevTools } from 'redux-devtools-extension';
import storageSession from 'redux-persist/lib/storage/session';
import logger from 'redux-logger';
import thunk from 'redux-thunk';

import rootReducer from './rootReducer';

const persistConfig = {
  key: 'root',
  storage: storageSession,
}

const persistedReducer = persistReducer(persistConfig, rootReducer);

// Not working. Look into it later. Help maybe? https://dev.to/dawnind/persist-redux-state-with-redux-persist-3k0d
// const serializableMiddleware = createSerializableStateInvariantMiddleware({
//   ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
// })

const middleware = applyMiddleware(thunk, logger);

const store = createStore(persistedReducer, composeWithDevTools(middleware));

const persistor = persistStore(store);

export { store, persistor };
