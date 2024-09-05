const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

// Firestore trigger function for document writes
exports.firestoreTrigger = functions.firestore
    .document('AppUsers/{userId}')  // Specify the Firestore collection and document path
    .onWrite((change, context) => {
        // The document that was written
        const newValue = change.after.exists ? change.after.data() : null;
        const previousValue = change.before.exists ? change.before.data() : null;

        // Log details of the Firestore event
        console.log('Document ID:', context.params.userId);
        console.log('New Value:', newValue);
        console.log('Previous Value:', previousValue);

        // Perform any additional operations here, if needed

        return null;
    });

