import '/auth/firebase_auth/auth_util.dart';
import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class SetKeywordsModel extends FlutterFlowModel {
  ///  State fields for stateful widgets in this component.

  final formKey = GlobalKey<FormState>();
  // State field(s) for firstname widget.
  TextEditingController? firstnameController;
  String? Function(BuildContext, String?)? firstnameControllerValidator;
  // State field(s) for lastname widget.
  TextEditingController? lastnameController;
  String? Function(BuildContext, String?)? lastnameControllerValidator;
  // State field(s) for phone widget.
  TextEditingController? phoneController;
  String? Function(BuildContext, String?)? phoneControllerValidator;
  // State field(s) for keyword widget.
  TextEditingController? keywordController;
  String? Function(BuildContext, String?)? keywordControllerValidator;
  // Stores action output result for [Backend Call - API (Add Keyword )] action in Button widget.
  ApiCallResponse? apiResult6ou;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {}

  void dispose() {
    firstnameController?.dispose();
    lastnameController?.dispose();
    phoneController?.dispose();
    keywordController?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
