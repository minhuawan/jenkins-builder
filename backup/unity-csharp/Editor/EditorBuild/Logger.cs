using System.Linq;
using UnityEngine;

namespace EditorBuild
{
    public class Logger
    {
        private string name;

        public static Logger GetLogger<T>()
        {
            var name = typeof(T).FullName;
            var logger = new Logger(name);
            return logger;
        }

        public Logger(string name)
        {
            this.name = name;
        }

        public void Log(string message)
        {
            WriteLog(LogType.Log, message);
        }

        public void Error(string message)
        {
            WriteLog(LogType.Error, message);
        }

        private void WriteLog(UnityEngine.LogType logType, string message)
        {
            if (UnityEngine.Application.isBatchMode)
            {
                var type = logType.ToString().Substring(0, 1).ToUpper();
                var now = System.DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss.fff");
                // [2022-10-22 16:31:00 D@EditorBuildHelper] - Hello world
                var msg = $"[{now} {type}@{name}] - {message}";
                System.Console.WriteLine(msg);
            }
            else
            {
                UnityEngine.Debug.unityLogger.Log(logType, message);
            }
        }
    }
}