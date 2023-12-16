import 'dart:convert';

import 'package:flutter/services.dart';

Future<Map<String, dynamic>> loadJson({required String path}) async {
  final file = await rootBundle.loadString(path);
  return jsonDecode(file);
}
