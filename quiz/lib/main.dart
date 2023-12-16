import 'package:card_swiper/card_swiper.dart';
import 'package:flutter/material.dart';

import 'package:quiz/flip_image.dart';
import 'package:quiz/utils/load_json.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'FlipCard',
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Oyaji Gag Quiz',
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
      ),
      body: FutureBuilder(
          future: loadJson(path: 'assets/json/quiz.json'),
          builder: (context, snapshot) {
            if (snapshot.hasError) return Text(snapshot.error.toString());

            if (snapshot.hasData) {
              final data = snapshot.data as Map<String, dynamic>;
              final quiz = data['quiz'] as List<dynamic>;
              return Swiper(
                itemBuilder: (context, index) => FlipImage(
                    text: quiz[index]['text'] as String,
                    imageName: quiz[index]['image_name'] as String,
                    hint: quiz[index]['hint'] as String),
                itemCount: quiz.length,
                scrollDirection: Axis.vertical,
              );
            }

            return const Center(child: CircularProgressIndicator());
          }),
    );
  }
}
