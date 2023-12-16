import 'package:flip_card/flip_card.dart';
import 'package:flutter/material.dart';

class FlipImage extends StatelessWidget {
  const FlipImage({super.key, required this.text, required this.imageName, required this.hint});

  final String text;
  final String imageName;
  final String hint;

  _renderContent(context) {
    return Card(
      elevation: 0.0,
      margin: const EdgeInsets.only(left: 32.0, right: 32.0, top: 20.0, bottom: 0.0),
      child: FlipCard(
        direction: FlipDirection.HORIZONTAL,
        side: CardSide.FRONT,
        speed: 700,
        front: Container(
          decoration: BoxDecoration(
            borderRadius: const BorderRadius.all(Radius.circular(8.0)),
            image: DecorationImage(
              image: AssetImage('assets/images/$imageName'),
              fit: BoxFit.fitWidth,
            ),
          ),
        ),
        back: Container(
          decoration: BoxDecoration(
            color: Colors.lightGreen[100],
            borderRadius: const BorderRadius.all(Radius.circular(8.0)),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('答え', style: Theme.of(context).textTheme.headlineLarge),
              const SizedBox(height: 20.0),
              Text(text, style: Theme.of(context).textTheme.headlineSmall),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: <Widget>[
        Center(
            child: Padding(
          padding: const EdgeInsets.only(top: 16.0),
          child: Text('画像から答えを推測しよう！', style: Theme.of(context).textTheme.headlineSmall),
        )),
        Expanded(child: _renderContent(context)),
        Expanded(
          child: Wrap(
            children: [
              Padding(
                padding: const EdgeInsets.all(32.0),
                child: Theme(
                  data: Theme.of(context).copyWith(dividerColor: Colors.transparent),
                  child: ClipRRect(
                    borderRadius: const BorderRadius.all(Radius.circular(8.0)),
                    child: ExpansionTile(
                      title: const Text('ヒント💡', style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                      backgroundColor: Colors.amber[50],
                      collapsedBackgroundColor: Colors.amber[50],
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.all(16.0),
                          child: Text(hint, style: Theme.of(context).textTheme.headlineLarge),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
