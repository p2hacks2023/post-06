import 'package:flutter/material.dart';

import 'package:flip_card/flip_card.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'FlipCard',
      // theme: ThemeData.li(),
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  _renderContent(context) {
    return Card(
      elevation: 0.0,
      margin: const EdgeInsets.only(left: 32.0, right: 32.0, top: 20.0, bottom: 0.0),
      // color: Color(0x00000000),
      child: FlipCard(
        direction: FlipDirection.HORIZONTAL,
        side: CardSide.FRONT,
        speed: 700,
        onFlipDone: (status) {
          // print(status);
        },
        front: Container(
          decoration: const BoxDecoration(
            borderRadius: BorderRadius.all(Radius.circular(8.0)),
            image: DecorationImage(
              image: AssetImage('assets/images/GBMbep8bMAAsgj0.jpeg'),
              fit: BoxFit.fill,
            ),
          ),
        ),
        back: Container(
          decoration: const BoxDecoration(
            color: Color(0xFF006666),
            borderRadius: BorderRadius.all(Radius.circular(8.0)),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('答え', style: Theme.of(context).textTheme.headlineLarge),
              const SizedBox(height: 20.0),
              Text('レモンの入れもん',
                  style: Theme.of(context).textTheme.bodyLarge),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Quiz'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          // _renderAppBar(context),
          Expanded(
            // flex: 4,
            child: _renderContent(context),
          ),
          const Expanded(
            // flex: 1,
            child: SizedBox.expand(),
          ),
        ],
      ),
    );
  }
}