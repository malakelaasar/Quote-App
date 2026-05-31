import 'package:flutter/material.dart';

void main() {
  runApp(const QuoteApp());
}

class QuoteApp extends StatelessWidget {
  const QuoteApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Daily Inspiration',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF1B8A7A),
          brightness: Brightness.light,
        ),
        fontFamily: 'Roboto',
      ),
      home: const QuoteHomePage(),
    );
  }
}

class QuoteHomePage extends StatefulWidget {
  const QuoteHomePage({super.key});

  @override
  State<QuoteHomePage> createState() => _QuoteHomePageState();
}

class _QuoteHomePageState extends State<QuoteHomePage> {
  int currentIndex = 0;

  final List<String> quotes = const [
    'Small steps every day lead to big results.',
    'Your attitude determines your direction.',
    'Stay patient and trust your journey.',
    'Discipline is choosing what you want most over what you want now.',
    'Great things never come from comfort zones.',
  ];

  final List<String> imagePaths = const [
    'assets/images/quote_steps.png',
    'assets/images/quote_direction.png',
    'assets/images/quote_journey.png',
    'assets/images/quote_discipline.png',
    'assets/images/quote_comfort_zone.png',
  ];

  void showNextQuote() {
    setState(() {
      currentIndex = (currentIndex + 1) % quotes.length;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Daily Inspiration',
          style: TextStyle(fontWeight: FontWeight.w700, color: Colors.white),
        ),
        centerTitle: true,
        elevation: 0,
        backgroundColor: const Color(0xFF13756A),
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      body: Container(
        width: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFFE3FFF8), Color(0xFFC7F4EA), Color(0xFFFFFFFF)],
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  const SizedBox(height: 10),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 14,
                      vertical: 8,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.65),
                      borderRadius: BorderRadius.circular(30),
                    ),
                    child: const Row(
                      mainAxisSize: MainAxisSize.min,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.auto_awesome,
                          size: 20,
                          color: Color(0xFF13756A),
                        ),
                        SizedBox(width: 8),
                        Text(
                          'Motivation for today',
                          style: TextStyle(
                            color: Color(0xFF263238),
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(26),
                    child: Container(
                      height: 260,
                      decoration: BoxDecoration(
                        color: const Color(0xFFEAF7F3),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.12),
                            blurRadius: 18,
                            offset: const Offset(0, 10),
                          ),
                        ],
                      ),
                      child: Image.asset(
                        imagePaths[currentIndex],
                        fit: BoxFit.cover,
                        width: double.infinity,
                      ),
                    ),
                  ),
                  const SizedBox(height: 28),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 24,
                      vertical: 30,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(24),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.08),
                          blurRadius: 24,
                          offset: const Offset(0, 12),
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        const Icon(
                          Icons.lightbulb,
                          color: Color(0xFF21A790),
                          size: 38,
                        ),
                        const SizedBox(height: 18),
                        Text(
                          quotes[currentIndex],
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            color: Color(0xFF263238),
                            fontSize: 24,
                            height: 1.35,
                            fontWeight: FontWeight.w700,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 26),
                  FilledButton.icon(
                    onPressed: showNextQuote,
                    icon: const Icon(Icons.navigate_next),
                    label: const Text('Next Quote'),
                    style: FilledButton.styleFrom(
                      backgroundColor: const Color(0xFF13756A),
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(vertical: 17),
                      textStyle: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w700,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(18),
                      ),
                    ),
                  ),
                  const SizedBox(height: 18),
                  Text(
                    '${currentIndex + 1} / ${quotes.length}',
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      color: Color(0xFF4F6360),
                      fontSize: 15,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
